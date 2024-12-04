#!/bin/bash

# Initialize variables
NAME=""
LANGUAGE=""
EXTENSION=""

# Function to display usage information
usage() {
    echo "Usage: $0 --name NAME [--python | --javascript | --c | --cpp | --rust | --golang | --typescript]"
    exit 1
}

# Check if at least two arguments are provided
if [ $# -lt 2 ]; then
    usage
fi

# Parse command-line arguments
while [[ $# -gt 0 ]]; do
    key="$1"
    case $key in
        --name)
            NAME="$2"
            shift # past argument
            shift # past value
            ;;
        --python)
            LANGUAGE="python"
            EXTENSION="py"
            shift # past argument
            ;;
        --javascript)
            LANGUAGE="javascript"
            EXTENSION="js"
            shift # past argument
            ;;
        --c)
            LANGUAGE="c"
            EXTENSION="c"
            shift # past argument
            ;;
        --cpp)
            LANGUAGE="cpp"
            EXTENSION="cpp"
            shift # past argument
            ;;
        --rust)
            LANGUAGE="rust"
            EXTENSION="rs"
            shift # past argument
            ;;
        --golang)
            LANGUAGE="golang"
            EXTENSION="go"
            shift # past argument
            ;;
        --typescript)
            LANGUAGE="typescript"
            EXTENSION="ts"
            shift # past argument
            ;;
        --java)
            LANGUAGE="java"
            EXTENSION="java"
            shift # past argument
            ;;
        *)
            # Unknown option
            usage
            ;;
    esac
done

# Check if NAME and LANGUAGE are set
if [ -z "$NAME" ] || [ -z "$LANGUAGE" ]; then
    usage
fi

# Create the main directory
mkdir -p "$NAME"
cd "$NAME" || exit 1

# Create subdirectories and solution files
for dir in $(seq -w 1 25); do
    mkdir -p "$dir"
    touch "$dir/solution_part1.$EXTENSION"
    touch "$dir/solution_part2.$EXTENSION"
done

echo "Setup complete for '$NAME' using '$LANGUAGE'."

