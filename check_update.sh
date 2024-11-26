#!/bin/sh
git ls-remote --tags https://github.com/ArtifexSoftware/mupdf.git 2>/dev/null |awk '{ print $2; }' |sed -e 's|^refs/tags/||' |grep -vE -- '-(alpha|beta|rc)' |grep '^[0-9]' |sort -V |tail -n1
