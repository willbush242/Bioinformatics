#!/usr/bin/env bash
GENOME_DIR="/mnt/d/Input_Genomes"
OUTDIR="/mnt/d/Output_BRAKER"
BRAKER="/path/to/braker.pl"

mkdir -p "$OUTDIR"

for g in "$GENOME_DIR"/*.fasta
do
    name=$(basename "$g" .fasta)

    echo "Running BRAKER ES-mode (no optimisation) on $name"

    "$BRAKER" \
        --genome="$g" \
        --species="$name" \
        --esmode \
        --skipOptimize \
        --workingdir="$OUTDIR/$name" \
        --threads=8

done
