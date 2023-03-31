### Genomics Data source and download instructions

- XENA
  - TCGA-Target-GTex 
    - Combined page: `https://xenabrowser.net/datapages/?cohort=TCGA%20TARGET%20GTEx&removeHub=https%3A%2F%2Fxena.treehouse.gi.ucsc.edu%3A443`
    - tpm: `https://toil-xena-hub.s3.us-east-1.amazonaws.com/download/TcgaTargetGtex_rsem_gene_tpm.gz`
    - id_annotation:  `https://toil-xena-hub.s3.us-east-1.amazonaws.com/download/probeMap%2Fgencode.v23.annotation.gene.probemap`
      - rename `cp data/probeMap%2Fgencode.v23.annotation.gene.probemap data/gencode.v23.annotation.gene.probemap.tsv`
    - sample_annotation: `https://toil-xena-hub.s3.us-east-1.amazonaws.com/download/TCGA_GTEX_category.txt`
    - sample_phenotype: `https://toil-xena-hub.s3.us-east-1.amazonaws.com/download/TcgaTargetGTEX_phenotype.txt.gz`