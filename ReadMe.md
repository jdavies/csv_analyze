# CSV_Analyze

This is a python utility to run on CSV files generated by `DSBulk unload` to get a
quick analysis of the table, its fields and the largest size of each field. Using
this, you can quickly see if any field exceeds the 10MB Astra guardrail limit.

## Usage

```sh
python csv_analyze <filename.csv>
```

It will provide output similar to the following:

```sh
<Filename>
Field Name   Max Size
==========   ========
id           16b
blob         12K
big_blob     8M
```
