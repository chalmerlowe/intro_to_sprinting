#!/usr/bin/env python

import collections
import logging
import os
import re


log = logging.getLogger(__name__)


HIERARCHY = ('Table of Contents', './README.md', (
    ('Course Overview and Preparation', './prereq_overview.md', (
        # ('Instructor Preparation', './prereq_instructor.md', ()),
        # ('Student Preparation', './prereq_student.md', ()),
    )),
    # ('Environment Set-up', './environment_overview.md', (
    #     ('Installing the Software You\'ll Need', './installing_tools.md', ()),
    #     ('Setting up Virtual Environments', './virtual_environments.md', ()),
    #     ('Setting up GitHub and Forking a Repository', './github_setup.md', ()),
    #     ('Setting up Git', './git_config.md', ()),
    # )),
    # ('Using Git', './git_overview.md', (
    #     ('Git Concepts', './git_concepts.md', ()),
    #     ('Cloning a Repository', './git_cloning.md', ()),
    #     ('Git Primary Workflow: Add, Commit, Push', './git_main_lifecycle.md', ()),
    #     ('Git Common Operations', './git_common_operations.md', ()),
    #     ('Branching and Merging', './git_branch_merge.md', ()),
    # )),
    # ('Using GitHub', './github_overview.md', (
    #     ('GitHub Concepts', './github_concepts.md', ()),
    #     ('Submitting a Pull Request', './github_submit_pull_request.md', ()),
    # )),
))

TITLE_TAGS = ('<div id="title" comment="this section is auto-generated, do not manually edit">', '</div>')
NAV_TAGS = ('<div id="nav-links" comment="this section is auto-generated, do not manually edit">', '</div>')
NAV_CONTENT = '''\\1
| Previous | Up | Next |
|:---------|:---:|-----:|
| [{prev_title}]({prev_url}) | [{up_title}]({up_url}) | [{next_title}]({next_url}) |
\\2'''

TITLE_REGEX = re.compile(f'({TITLE_TAGS[0]})\s+.*?\s+({TITLE_TAGS[1]})', re.MULTILINE | re.DOTALL)
NAV_REGEX = re.compile(f'({NAV_TAGS[0]})\s+.*?\s+({NAV_TAGS[1]})', re.MULTILINE | re.DOTALL)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
CONTENT_DIR = os.path.join(BASE_DIR, 'class_materials')

NODES_BY_PATH = {}


Node = collections.namedtuple('Node', ['title', 'filename', 'parent', 'children'])


def make_subtree(item, parent):
    log.debug('creating node for %s', item[1] if item[1] else 'ROOT')
    assert item[1] not in NODES_BY_PATH or exit('repeated page: ' + item[1])
    node = Node(
        title=item[0],
        filename=item[1],
        parent=parent[1] if parent else None,
        children=tuple(make_subtree(x, item) for x in item[2]),
    )
    NODES_BY_PATH[item[1]] = node
    return node


def main():
    log.info('building page hierarchy tree')
    tree = make_subtree(HIERARCHY, None)
    log.debug('tree: %s', tree)
    log.debug('pages by path: %s', NODES_BY_PATH)
    all_filenames = set(k for k in NODES_BY_PATH.keys() if k)
    log.info('loading files from: %s', CONTENT_DIR)
    all_files = set(f'./{fname}' for fname in os.listdir(CONTENT_DIR) if re.match('[^.].*\.md', fname))
    log.debug('files: %s', all_files)
    for fname in sorted(all_filenames):
        if fname not in all_files:
            log.critical('hierarchy refers to non-existent page: %s', fname)
    for fname in all_files:
        if fname in NODES_BY_PATH:
            fpath = os.path.join(CONTENT_DIR, fname)
            with open(fpath) as fin:
                content = fin.read()
            node = NODES_BY_PATH[fname]
            log.info('node: %s', node.title)
            parent = NODES_BY_PATH[node.parent] if node.parent else None
            log.info('parent: %s', parent.title if parent else None)
            prev = node
            nxt = node
            new_nav = NAV_CONTENT.format(
                prev_title=prev.title,
                prev_url=prev.filename,
                up_title=parent.title if parent else None,
                up_url=parent.filename if parent else None,
                next_title=nxt.title,
                next_url=nxt.filename,
            )
            log.critical(new_nav)
            content = re.sub(NAV_REGEX, new_nav, content)
            log.critical(content)
            with open(fpath, 'w') as fout:
                fout.write(content)
        else:
            log.warning('skipping file %s (not in page structure)', fname)


if __name__ == '__main__':
    log.addHandler(logging.StreamHandler())
    log.setLevel(os.environ.get('LOGLEVEL', 'INFO'))
    main()