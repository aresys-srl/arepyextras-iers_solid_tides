#!/bin/bash
if [ "${CI_DEBUG_TRACE}" = "true" ]; then
    set -x
fi

set -euo pipefail
IFS=$'\n\t'

print_usage() {
    echo "SOLIDTools test driver script"
    echo "  test_driver.sh [options]"
    echo ""
    echo "Options:"
    echo "  -h --help                            print this help message"
    echo "  -v --verbose                         increase verbosity of this script"
    echo ""
    echo "  --exec=...                           test executable"
    echo "  --reference=...                      reference output file"
    echo "  --difference=....                    generated output file"
    echo ""
}

die() {
    printf '%s\n' "$1" >&2
    exit 1
}

verbose() {
    if [ "${VERBOSE+false}" = "true" ]; then
        printf '%s\n' "$1" >&1
    fi
}

# Parse command line arguments
if [ $# -lt 1 ]; then
    print_usage
    exit 1
fi

while (($#)); do
    case $1 in
        -h|--help)
            print_usage
            exit 0
            ;;
        -v|--verbose)
            VERBOSE="true"
            ;;
        --exec=?*)
            EXEC="${1#*=}"
            ;;
        --reference=?*)
            REFERENCE="${1#*=}"
            ;;
        --difference=?*)
            DIFFERENCE="${1#*=}"
            ;;
        -*)
            die "unknown flag $1"
            ;;
        *)
            break
            ;;
    esac
    shift
done

# check arguments
if [[ ! -f "$EXEC" ]]; then
    die "Test executable does not exist"
fi

if [[ ! -f "$REFERENCE" ]]; then
    die "Reference output file does not exist"
fi

if [[ -f "$DIFFERENCE" ]]; then
    verbose "Removing existing generated output file"
    rm "$DIFFERENCE"
fi

# run test
${EXEC} ${DIFFERENCE}
if [[ $? -ne 0 ]]; then
    die "Test execution failed"
fi

# check results
diff ${REFERENCE} ${DIFFERENCE}
if [[ $? -ne 0 ]]; then
    die "Output files are different"
fi
