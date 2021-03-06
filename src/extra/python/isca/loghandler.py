import logging

log = logging.getLogger('isca')
log.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
log.addHandler(ch)

def clean_log_info(s):
    if s.strip():
       log.info(s.strip())

def clean_log_error(s):
    if s.strip():
       log.error(s.strip())

def clean_log_debug(s):
    if s.strip():
       log.debug(s.strip())



class Logger(object):
    """A mixin for objects that wrap underlying processes that output to stdout."""
    log = log
    def clean_log(self, line):
        # Tidy up a std out line.  Returns None if blank.
        s = line.strip()
        return s if s else None

    def _on_stdout(self, line):
        """If the object has a 'on_stdout' method, use that.  Otherwise,
        echo the clean line to the stdout."""
        line = self.clean_log(line)
        if line:
            if hasattr(self, 'on_stdout'):
                self.on_stdout(line)
            else:
                self.log.info(line)

    def _on_stderr(self, line):
        """If the object has a 'on_stderr' method, use that.  Otherwise,
        echo the clean line to the stdout as a warning."""
        line = self.clean_log(line)
        if line:
            if hasattr(self, 'on_stderr'):
                self.on_stdout(line)
            else:
                self.log.warn(line)

