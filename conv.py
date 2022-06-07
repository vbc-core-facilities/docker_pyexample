#!/usr/bin/env python3

"""
BED-to-GFF conversion script.
:author: András Aszódi
:date: 2020-11-27
Copy of the script from the Python language course
see `pytraining/lang/script/dev/full/conv.py`
"""

# Conventional `import` statement ordering:
#  - Standard Library packages/modules
#  - Third-party packages/modules
#  - Application-specific packages/modules
# Within these groups, alphabetical ordering is recommended.
# 1. Import modules
import argparse
import datetime
import os.path
import sys

from genreg.region import Region

# 2. Parse command-line arguments
# 2A. Set up the parser
parser = argparse.ArgumentParser(description="BED to GFF file converter")

# 2B. Positional arguments: 1 or more input file names
parser.add_argument("bedfile", nargs='+')  # >=1 file names required

# 2D. Optional argument: if -w or --overwrite is specified,
# existing output file(s) will be overwritten
parser.add_argument("-w", "--overwrite",
                    action="store_true",
                    default=False,
                    help="Overwrite existing GFF output file")

# 2E. Optional argument: -s or --source sets the GFF "source" field
# the default is "conv"
parser.add_argument("-s", "--source",
                    default="conv",
                    help="The GFF 'source' field")

# 2C. Parse the arguments, save results in `args` object
args = parser.parse_args()

# 3. Get today's date as a string
# to be included in the GFF output
# looks like "2020-11-27"
datestr = datetime.date.today().isoformat()

# 4. Iterate over all positional arguments, i.e. the input file names
for bednm in args.bedfile:
    # 4A. Diagnostic message
    print("Processing", bednm)

    # 4B. If the input file is non-existent,
    # print an error message and continue
    if not os.path.exists(bednm):
        print("Cannot read from", bednm)
        continue

    # 5. Create output file name
    basenm, oldext = os.path.splitext(bednm)
    gffnm = basenm + ".gff"

    # 6. Check if output file exists
    if os.path.exists(gffnm):
        if args.overwrite:
            # output may be overwritten, but let the user know
            print(gffnm, "will be overwritten")
        else:
            # may not be overwritten
            print(gffnm, "exists, skip")
            continue

    # 7. Open input and output files (nested `with`)
    with open(bednm) as inf, open(gffnm, mode="w") as outf:
        # print GFF header to output
        print("##gff-version 2", file=outf)
        print("##date", datestr, file=outf)

        # 8. Conversion
        # 8A. Create an empty Region instance
        reg = Region()

        # 8B. Iterate over the input file's lines
        for bedline in inf:
            try:
                # 8C. Reading and writing
                # Delete `pass` before coding this part!
                ok = reg.from_bed(bedline)
                if ok:
                    gffline = reg.to_gff(args.source)
                else:
                    gffline = bedline
                print(gffline, file=outf)
            except ValueError:
                # 8D. Error handling
                # Delete `pass` before coding this part!
                bad = "### Malformed line: " + bedline
                print(bad, file=sys.stderr)
                print(bad, file=outf)
        # end for
    # `with` closes outf, inf implicitly
    # closing diagnostics message
    print("Wrote", gffnm)
