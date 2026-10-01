#!/usr/bin/env bash
GENOME_DIR="/mnt/d/Input_Genomes"
OUTDIR="/mnt/d/Output_BRAKER"
TEMPLATE="/mnt/d/Input_Proteins/reference_proteins.faa"
BRAKER="/path/to/braker.pl"

mkdir -p "$OUTDIR"

for g in "$GENOME_DIR"/*.fasta
do
    name=$(basename "$g" .fasta)

    echo "Running BRAKER on $name"

    "$BRAKER" \
        --genome="$g" \
        --species=chlamy \
        --useexisting \
        --prot_seq="$TEMPLATE" \
        --workingdir="$OUTDIR/$name" \
        --threads=8
done
