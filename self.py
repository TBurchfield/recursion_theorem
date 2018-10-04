#!/usr/bin/env python3

# This program prints its own source code.
# It is based on Sipsers construction on page 247

# setting x corresponds to what A does in SELF
x = '''print("""#!/usr/bin/env python3

# This program prints its own source code.
# It is based on Sipsers construction on page 247

# setting x corresponds to what A does in SELF
x = \'\'\'{}\'\'\'
# This section corresponds to the execution of B in SELF
{}
""".format(x.replace("\\\\", "\\\\\\\\").replace("\'", "\\\\\'"), x), end=\'\')'''
# This section corresponds to the execution of B in SELF
print("""#!/usr/bin/env python3

# This program prints its own source code.
# It is based on Sipsers construction on page 247

# setting x corresponds to what A does in SELF
x = '''{}'''
# This section corresponds to the execution of B in SELF
{}
""".format(x.replace("\\", "\\\\").replace("'", "\\'"), x), end='')
