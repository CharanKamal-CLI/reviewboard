import subprocess
import urllib2
from reviewboard.scmtools import sshutils
from reviewboard.scmtools.core import SCMTool, HEAD, PRE_CREATION
        SCMTool.__init__(self, repository)
        self.client = GitClient(repository.path, repository.raw_file_url)
    def parse_diff_revision(self, file_str, revision_str):
        elif revision != PRE_CREATION:
    def check_repository(cls, path, username=None, password=None):
        client = GitClient(path)
        super(GitTool, cls).check_repository(client.path, username, password)
            i, file_info = self._parse_diff(i)
        """
        Parses out one file from a Git diff
            return self._parse_git_diff(linenum)
            return linenum + 1, None
        try:
            if self._is_empty_change(linenum):
                linenum += GIT_DIFF_EMPTY_CHANGESET_SIZE
                return linenum, None
        except IndexError:
            # This means this is the only bit left in the file
            linenum += GIT_DIFF_EMPTY_CHANGESET_SIZE
            return linenum, None
        # We have no use for recording this info so skip it
        if self._is_newfile_or_deleted_change(linenum):
        next_diff_start = self.lines[linenum + GIT_DIFF_EMPTY_CHANGESET_SIZE]
    def _is_newfile_or_deleted_change(self, linenum):
        line = self.lines[linenum]
        return (line.startswith("new file mode")
                or line.startswith("deleted file mode"))
        return (line.startswith("Binary files") or
class GitClient(object):
    def __init__(self, path, raw_file_url=None):
        self.path = self._normalize_git_url(path)
            # First, try to grab the file remotely.
            try:
                url = self._build_raw_url(path, revision)
                return urllib2.urlopen(url).read()
            except Exception, e:
                logging.error("Git: Error fetching file from %s: %s" % (url, e))
                raise SCMError("Error fetching file from %s: %s" % (url, e))
            self.validate_sha1_format(path, revision)

            # First, try to grab the file remotely.
                url = self._build_raw_url(path, revision)
                return urllib2.urlopen(url).geturl()
            except urllib2.HTTPError, e:
                if e.code != 404:
                    logging.error("Git: HTTP error code %d when fetching "
                                  "file from %s: %s" % (e.code, url, e))
            except Exception, e:
                logging.error("Git: Error fetching file from %s: %s" % (url, e))

            return False
        return subprocess.Popen(
            ['git'] + args,
            stderr=subprocess.PIPE,
            stdout=subprocess.PIPE,
            close_fds=(os.name != 'nt')
        )
            return 'ssh://%s%s%s' % (m.group('username'),