#!/usr/bin/env python3
import os
import re
import subprocess
import sys
from pathlib import PurePosixPath

SOURCE_EXTENSIONS = {
    '.py','.pyx','.js','.mjs','.cjs','.jsx','.ts','.tsx','.java','.kt','.kts','.swift',
    '.go','.rs','.c','.cc','.cpp','.cxx','.h','.hh','.hpp','.hxx','.cs','.php','.rb',
    '.dart','.scala','.lua','.r','.pl','.pm','.sh','.bash','.zsh','.fish','.ps1','.psm1',
    '.sql','.vue','.svelte','.sol','.tf','.tfvars','.proto'
}

FORBIDDEN_BASENAMES = {
    '.env','id_rsa','id_dsa','id_ecdsa','id_ed25519','credentials.json','secrets.json',
    'google-services.json','googleservice-info.plist','service-account.json','service_account.json'
}

FORBIDDEN_SUFFIXES = {'.pem','.key','.p12','.pfx','.jks','.keystore','.ovpn'}
FORBIDDEN_PATH_PARTS = {'src','source','lib','app','server','backend','frontend','database','migrations'}

ALLOWED_SOURCE_EXCEPTIONS = {
    '.github/scripts/public_repository_guard.py',
}

SECRET_PATTERNS = [
    ('private-key', re.compile(r'-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----')),
    ('github-token', re.compile(r'\bgh(?:p|o|u|s|r)_[A-Za-z0-9_]{30,}\b')),
    ('aws-access-key', re.compile(r'\bAKIA[0-9A-Z]{16}\b')),
    ('google-api-key', re.compile(r'\bAIza[0-9A-Za-z\-_]{35}\b')),
    ('stripe-live-key', re.compile(r'\b(?:sk|rk)_live_[0-9A-Za-z]{16,}\b')),
    ('slack-token', re.compile(r'\bxox[baprs]-[0-9A-Za-z-]{10,}\b')),
    ('jwt', re.compile(r'\beyJ[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\b')),
    ('credential-in-url', re.compile(r'\b(?:https?|postgres(?:ql)?|mysql|mongodb(?:\+srv)?)://[^\s/:]+:[^\s/@]+@')),
    ('sensitive-assignment', re.compile(
        r'(?i)\b(?:api[_-]?key|secret|token|password|passwd|client[_-]?secret|private[_-]?key|service[_-]?role)\b\s*[:=]\s*["\'](?!example|placeholder|changeme|redacted|<)[^"\']{8,}["\']'
    )),
]

TEXT_EXTENSIONS = {'.md','.txt','.yml','.yaml','.json','.toml','.ini','.cfg','.conf','.xml','.html','.css'}


def run(*args):
    return subprocess.check_output(args, text=True, stderr=subprocess.STDOUT)


def git_paths_for_commit(commit):
    out = run('git','ls-tree','-r','--name-only',commit)
    return [p for p in out.splitlines() if p]


def check_path(path):
    problems = []
    p = PurePosixPath(path)
    lower = path.lower()
    base = p.name.lower()
    suffix = p.suffix.lower()
    parts = {part.lower() for part in p.parts}

    if path in ALLOWED_SOURCE_EXCEPTIONS:
        return problems
    if base in FORBIDDEN_BASENAMES or base.startswith('.env.'):
        problems.append('sensitive filename')
    if suffix in FORBIDDEN_SUFFIXES:
        problems.append('sensitive key/certificate file')
    if suffix in SOURCE_EXTENSIONS:
        problems.append('source-code file')
    if parts & FORBIDDEN_PATH_PARTS:
        problems.append('source-code directory')
    if '/.git/' in f'/{lower}/':
        problems.append('embedded git metadata')
    return problems


def content_for(commit, path):
    try:
        return subprocess.check_output(['git','show',f'{commit}:{path}'], stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError:
        return b''


def check_content(commit, path):
    suffix = PurePosixPath(path).suffix.lower()
    if suffix not in TEXT_EXTENSIONS and not path.startswith('.github/workflows/'):
        return []
    raw = content_for(commit, path)
    if b'\x00' in raw or len(raw) > 2_000_000:
        return []
    text = raw.decode('utf-8', errors='ignore')
    hits = []
    for name, pattern in SECRET_PATTERNS:
        for match in pattern.finditer(text):
            line = text.count('\n', 0, match.start()) + 1
            hits.append(f'{name} at line {line}')
            if len(hits) >= 5:
                return hits
    return hits


def main():
    commits = run('git','rev-list','--all').splitlines()
    if not commits:
        print('No commits found; refusing to pass silently.', file=sys.stderr)
        return 2

    violations = []
    seen_blobs = set()
    for commit in commits:
        short = commit[:12]
        for path in git_paths_for_commit(commit):
            for problem in check_path(path):
                violations.append(f'{short} {path}: {problem}')

            try:
                blob = run('git','rev-parse',f'{commit}:{path}').strip()
            except subprocess.CalledProcessError:
                blob = f'{commit}:{path}'
            if blob in seen_blobs:
                continue
            seen_blobs.add(blob)
            for problem in check_content(commit, path):
                violations.append(f'{short} {path}: {problem}')

    if violations:
        print('PUBLIC REPOSITORY GUARD: BLOCKED', file=sys.stderr)
        for item in sorted(set(violations))[:200]:
            print(f'::error::{item}', file=sys.stderr)
        if len(violations) > 200:
            print(f'::error::Additional violations omitted: {len(violations)-200}', file=sys.stderr)
        return 1

    print(f'PUBLIC REPOSITORY GUARD: PASS | commits={len(commits)} | unique_blobs={len(seen_blobs)}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
