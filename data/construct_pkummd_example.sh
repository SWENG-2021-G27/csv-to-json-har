cat ../sample_header.json | tr '\n' '' > data/pkummd_example.json
python converter.py | tr '\n' '' >> data/pkummd_example.json
cat ../sample_footer.json | tr '\n' '' >> data/pkummd_example.json
