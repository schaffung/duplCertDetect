"""
Script to check the duplicate entried of certificates inside the
glusterfs.ca file.
"""

import sys
import os.path


CERT_BEGIN_LINE = "-----BEGIN CERTIFICATE-----"
CERT_END_LINE = "-----END CERTIFICATE-----"

# Cert Dict.
CERT_DICT = {}
CERT_COUNT = 0
CERT_VALUE = ""

if len(sys.argv) < 2:
    sys.exit("Certificate path not given")
else:
    CERT_FILE = sys.argv[1]

# Check if the path given comes out to a file.
if not os.path.isfile(CERT_FILE):
    sys.exit("Not a file")

fd = open(CERT_FILE)

for line in fd:
    # Strip the newline,
    line = line.rstrip("\n")
    if line == CERT_BEGIN_LINE:
        CERT_VALUE = ""
        CERT_VALUE += line
        CERT_COUNT += 1
    elif line == CERT_END_LINE:
        CERT_VALUE += line
        CERT_DICT[CERT_COUNT] = CERT_VALUE
    else:
        CERT_VALUE += line

fd.close()
# To find duplicates, let's flip the dictionary.
FLIPPED_CERT_DICT = {}

for key, value in CERT_DICT.items():
    if value not in FLIPPED_CERT_DICT:
        FLIPPED_CERT_DICT[value] = [key]
    else:
        FLIPPED_CERT_DICT[value].append(key)

# Now, we just need to find values with len more than 1.
for key, value in FLIPPED_CERT_DICT.items():
    if len(value) > 1:
        print("Duplicate Certificate found!", key)
        continue
