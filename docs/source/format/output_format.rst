Output format
=============

tags: ``Resimpy``
                 

1. fastq.gz
-----------

Simulated reads are stored in fastq.gz format. Please see
`here <https://en.wikipedia.org/wiki/FASTQ_format>`__ for details.

2. UMI, Barcode, genomic sequence records
-----------------------------------------

The ground-truth or initial generated UMIs, Barcodes, genomic sequences
are stored in txt format, respectively.

``umi.txt`` \| UMI\| \| ———— \| \| AATTTTCCT… \| \| CTCATCCTC… \| \| …
\|

``barcode.txt`` \| \| \| ———— \| \| TGTGCCCGG… \| \| TCATCCCTC… \| \| …
\|

``seq.txt`` \| seq\| \| ———— \| \| ATCCTCCTC… \| \| GCAATCCGA… \| \| …
\|
