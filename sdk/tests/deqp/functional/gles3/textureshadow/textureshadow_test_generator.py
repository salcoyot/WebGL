#!/usr/bin/env python

# Copyright (c) 2016 The Khronos Group Inc.
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and/or associated documentation files (the
# "Materials"), to deal in the Materials without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Materials, and to
# permit persons to whom the Materials are furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Materials.
#
# THE MATERIALS ARE PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# MATERIALS OR THE USE OR OTHER DEALINGS IN THE MATERIALS.

"""
  Generator for textureformat* tests.
  This file needs to be run in its folder.
"""

import sys

_DO_NOT_EDIT_WARNING = """<!--

This file is auto-generated from textureshadow_test_generator.py
DO NOT EDIT!

-->

"""

_HTML_TEMPLATE = """<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<title>WebGL Texture Shadow Conformance Tests</title>
<link rel="stylesheet" href="../../../../resources/js-test-style.css"/>
<script src="../../../../js/js-test-pre.js"></script>
<script src="../../../../js/webgl-test-utils.js"></script>

<script src="../../../../closure-library/closure/goog/base.js"></script>
<script src="../../../deqp-deps.js"></script>
<script>goog.require('functional.gles3.es3fTextureShadowTests');</script>
</head>
<body>
<div id="description"></div>
<div id="console"></div>
<canvas id="canvas" width="200" height="100"> </canvas>
<script>
var wtu = WebGLTestUtils;
var gl = wtu.create3DContext('canvas', null, 2);

functional.gles3.es3fTextureShadowTests.run(gl, [%(start)s, %(end)s]);
</script>
</body>
</html>
"""

_TARGETS = [
    '2d',
    'cube',
]

_FILTERS = [
    'nearest',
    'linear',
    'nearest_mipmap_nearest',
    'linear_mipmap_nearest',
    'nearest_mipmap_linear',
    'linear_mipmap_linear',
]

_COMPARE_FUNCS = [
    'less_or_equal',
    'greater_or_equal',
    'less',
    'greater',
    'equal',
    'not_equal',
    'always',
    'never',
]

def GenerateFilename(group):
  """Generate test filename."""
  filename = group
  filename += ".html"
  return filename

def WriteTest(filename, start, end):
  """Write one test."""
  file = open(filename, "wb")
  file.write(_DO_NOT_EDIT_WARNING)
  file.write(_HTML_TEMPLATE % {
    'start': start,
    'end': end
  })
  file.close

def GenerateTests():
  """Generate all tests."""
  filelist = []
  ii = 0
  for iTarget in range(len(_TARGETS)):
    for iFilter in range(len(_FILTERS)):
      for iFunc in range(len(_COMPARE_FUNCS)):
        item = _TARGETS[iTarget] + '_' + _FILTERS[iFilter] + '_' + _COMPARE_FUNCS[iFunc]
        filename = GenerateFilename(item)
        filelist.append(filename)
        WriteTest(filename, ii, ii + 1)
        ii = ii + 1
  return filelist

def GenerateTestList(filelist):
  file = open("00_test_list.txt", "wb")
  file.write('\n'.join(filelist))
  file.close

def main(argv):
  """This is the main function."""
  filelist = GenerateTests()
  GenerateTestList(filelist)

if __name__ == '__main__':
  sys.exit(main(sys.argv[1:]))
