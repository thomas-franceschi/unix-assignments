#!/bin/sh


# Configuration
CC=${CC:-gcc}
CFLAGS=${CFLAGS:--std=gnu99 -Wall}
SUFFIXES=${SUFFIXES:-.c}
VERBOSE=${VERBOSE:-0}

# Compile all files                                                                                                                                                                                    
for suffix in ${SUFFIXES}; do
    for src in *${suffix}; do
        tgt=$(basename ${src} ${suffix})
        [ "$VERBOSE" -gt 0 ] && echo ${CC} ${CFLAGS} -o ${tgt} ${src}
        ${CC} ${CFLAGS} -o ${tgt} ${src} || exit 1
    done
done
