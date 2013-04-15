from reviewboard.scmtools.core import SCMClient, SCMTool, HEAD, PRE_CREATION
from reviewboard.ssh import utils as sshutils
    supports_authentication = True
    field_help_text = {
        'path': 'For local Git repositories, this should be the path to a '
                '.git directory that Review Board can read from. For remote '
                'Git repositories, it should be the clone URL.',
    }
        super(GitTool, self).__init__(repository)

        local_site_name = None

        if repository.local_site:
            local_site_name = repository.local_site.name

        self.client = GitClient(repository.path, repository.raw_file_url,
                                repository.username, repository.password,
                                repository.encoding, local_site_name)
    def parse_diff_revision(self, file_str, revision_str, moved=False,
                            *args, **kwargs):
        elif revision != PRE_CREATION and not moved and revision != '':
            # Moved files with no changes has no revision,
            # so don't validate those.
    def check_repository(cls, path, username=None, password=None,
                         local_site_name=None):
        client = GitClient(path, local_site_name=local_site_name)
        super(GitTool, cls).check_repository(client.path, username, password,
                                             local_site_name)
        preamble = ''

            next_i, file_info, new_diff = self._parse_diff(i)


                if preamble:
                    file_info.data = preamble + file_info.data
                    preamble = ''

            elif new_diff:
                # We found a diff, but it was empty and has no file entry.
                # Reset the preamble.
                preamble = ''
            else:
                preamble += self.lines[i] + '\n'

            i = next_i

        """Parses out one file from a Git diff

        This will return a tuple of the next line number, the file info
        (if any), and whether or not we've found a file (even if we decided
        not to record it).
            parts = self._parse_git_diff(linenum)

            return parts[0], parts[1], True
            return linenum + 1, None, False
        empty_change = self._is_empty_change(linenum)
        empty_change_linenum = linenum + GIT_DIFF_EMPTY_CHANGESET_SIZE

        # Parse the extended header to save the new file, deleted file,
        # mode change, file move, and index.
        if self._is_new_file(linenum):
            file_info.data += self.lines[linenum] + "\n"
        elif self._is_deleted_file(linenum):
            file_info.data += self.lines[linenum] + "\n"
            linenum += 1
            file_info.deleted = True
            file_info.data += self.lines[linenum] + "\n"
            file_info.data += self.lines[linenum + 1] + "\n"
        elif self._is_moved_file(linenum):
            file_info.data += self.lines[linenum] + "\n"
            file_info.data += self.lines[linenum + 1] + "\n"
            file_info.data += self.lines[linenum + 2] + "\n"
            linenum += 3
            file_info.moved = True

        # Only show interesting empty changes. Basically, deletions.
        # It's likely a binary file if we're at this point, and so we want
        # to process the rest of it.
        if empty_change and not file_info.deleted:
            return empty_change_linenum, None
            file_info.data += self.lines[linenum] + "\n"
                file_info.data += self.lines[linenum] + "\n"
        next_diff_start_linenum = linenum + GIT_DIFF_EMPTY_CHANGESET_SIZE

        if next_diff_start_linenum >= len(self.lines):
            return True

        next_diff_start = self.lines[next_diff_start_linenum]
    def _is_new_file(self, linenum):
        return self.lines[linenum].startswith("new file mode")
    def _is_deleted_file(self, linenum):
        return self.lines[linenum].startswith("deleted file mode")
    def _is_moved_file(self, linenum):
        return (self.lines[linenum].startswith("similarity index") and
                self.lines[linenum + 1].startswith("rename from") and
                self.lines[linenum + 2].startswith("rename to"))

        return (line.startswith("Binary file") or
class GitClient(SCMClient):
    def __init__(self, path, raw_file_url=None, username=None, password=None,
                 encoding='', local_site_name=None):
        super(GitClient, self).__init__(self._normalize_git_url(path),
                                        username=username,
                                        password=password)

        self.encoding = encoding
        self.local_site_name = local_site_name
            return self.get_file_http(self._build_raw_url(path, revision),
                                      path, revision)
                # We want to make sure we can access the file successfully,
                # without any HTTP errors. A successful access means the file
                # exists. The contents themselves are meaningless, so ignore
                # them. If we do successfully get the file without triggering
                # any sort of exception, then the file exists.
                self.get_file(path, revision)
                return True
            except Exception:
                return False
        return SCMTool.popen(['git'] + args,
                             local_site_name=self.local_site_name)
            return 'ssh://%s%s%s' % (m.group('username') or '',