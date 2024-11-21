from git.repo.base import Repo
import argparse

def main():
    parser = argparse.ArgumentParser(description='Clone a repository.')
    parser.add_argument('--clone_url', type=str, help='The name of the repo to clone')
    parser.add_argument('--target', type=str, help='The target directory to clone the repo into')
    parser.add_argument('--branch', type=str, help='The branch to clone', default='main')
    args = parser.parse_args()
    Repo.clone_from(url=args.clone_url, to_path=args.target, branch=args.branch)
    
if __name__ == "__main__":
    main()
