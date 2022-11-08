#!/bin/sh
curl -L https://mupdf.com/downloads/archive/ 2>/dev/null |grep -E 'mupdf-.*-source.tar.gz' |sed -e 's,.*mupdf-,,;s,-source\.tar\.gz.*,,' |grep -E '^[0-9.]*$' |sort -V |tail -n1
