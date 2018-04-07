#!/usr/bin/env python

import collections
import logging
import os
import re


log = logging.getLogger(__name__)


HIERARCHY = (None, None, (
    ('Course Overview and Preparation', './prereq_overview.md', (
        ('Instructor Preparation', './prereq_instructor.md', ()),
        ('Student Preparation', './prereq_student.md', ()),
    )),
    ('Environment Set-up', './environment_overview.md', (
        ('''Installing the Software You'll Need''', './installing_tools.md', ()),
        ('Setting up Virtual Environments', './virtual_environments.md', ()),
        ('Setting up GitHub and Forking a Repository', './github_setup.md', ()),
        ('Setting up Git', './git_config.md', ()),
    )),
    ('Using Git', './git_overview.md', (
        ('Git Concepts', './git_concepts.md', ()),
        ('Cloning a Repository', './git_cloning.md', ()),
        ('Git Primary Workflow: Add, Commit, Push', './git_main_lifecycle.md', ()),
        ('Git Common Operations', './git_common_operations.md', ()),
        ('Branching and Merging', './git_branch_merge.md', ()),
    )),
    ('Using GitHub', './github_overview.md', (
        ('GitHub Concepts', './github_concepts.md', ()),
        ('Submitting a Pull Request', './github_submit_pull_request.md', ()),
    )),
))

TITLE_REGEX = re.compile('<title id="title" comment="this section is auto-generated, do not manually edit">(.*)</div>')  # noqa E501
NAV_REGEX = re.compile('<div id="nav-links" comment="this section is auto-generated, do not manually edit">(.*)</div>')  # noqa E501

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
CONTENT_DIR = os.path.join(BASE_DIR, 'class_materials')

PAGES_BY_PATH = {}


Node = collections.namedtuple('Node', ['title', 'filename', 'parent', 'children'])


def make_subtree(item, parent):
    log.debug('creating node for %s', item[1] if item[1] else 'ROOT')
    assert item[1] not in PAGES_BY_PATH or exit('repeated page: ' + item[1])
    PAGES_BY_PATH[item[1]] = item[:2]
    return Node(
        title=item[0],
        filename=item[1],
        parent=parent[1] if parent else None,
        children=tuple(make_subtree(x, item) for x in item[2]),
    )


def main():
    tree = make_subtree(HIERARCHY, None)
    log.debug('tree: %s', tree)
    all_filenames = set(PAGES_BY_PATH.keys())
    assert len(all_filenames) == len(PAGES_BY_PATH)
    log.debug('pages by path: %s', PAGES_BY_PATH)


if __name__ == '__main__':
    log.addHandler(logging.StreamHandler())
    log.setLevel(os.environ.get('LOGLEVEL', 'INFO'))
    main()