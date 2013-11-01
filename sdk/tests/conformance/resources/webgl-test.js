/*
** Copyright (c) 2012 The Khronos Group Inc.
**
** Permission is hereby granted, free of charge, to any person obtaining a
** copy of this software and/or associated documentation files (the
** "Materials"), to deal in the Materials without restriction, including
** without limitation the rights to use, copy, modify, merge, publish,
** distribute, sublicense, and/or sell copies of the Materials, and to
** permit persons to whom the Materials are furnished to do so, subject to
** the following conditions:
**
** The above copyright notice and this permission notice shall be included
** in all copies or substantial portions of the Materials.
**
** THE MATERIALS ARE PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
** EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
** MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
** IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
** CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
** TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
** MATERIALS OR THE USE OR OTHER DEALINGS IN THE MATERIALS.
*/

function getGLErrorAsString(ctx, err) {
  if (err === ctx.NO_ERROR) {
    return "NO_ERROR";
  }
  for (var name in ctx) {
    if (ctx[name] === err) {
      return name;
    }
  }
  return "0x" + err.toString(16);
}

// Pass undefined for glError to test that it at least throws some error
function shouldGenerateGLError(ctx, glErrors, evalStr) {
  if (!glErrors.length) {
    glErrors = [glErrors];
  }
  var exception;
  try {
    eval(evalStr);
  } catch (e) {
    exception = e;
  }
  if (exception) {
    testFailed(evalStr + " threw exception " + exception);
  } else {
    var err = ctx.getError();
    var errStrs = [];
    for (var ii = 0; ii < glErrors.length; ++ii) {
      errStrs.push(getGLErrorAsString(ctx, glErrors[ii]));
    }
    var expected = errStrs.join(" or ");
    if (glErrors.indexOf(err) < 0) {
      testFailed(evalStr + " expected: " + expected + ". Was " + getGLErrorAsString(ctx, err) + ".");
    } else {
      var msg = (glErrors.length == 1) ? " generated expected GL error: " :
                                         " generated one of expected GL errors: ";
      testPassed(evalStr + msg + expected + ".");
    }
  }
}

