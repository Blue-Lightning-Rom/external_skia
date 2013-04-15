{
  'includes': [
    'common.gypi',
  ],
  'targets': [
    {
      'target_name': 'animator',
      'type': 'static_library',
      'include_dirs': [
        '../include/config',
        '../include/core',
        '../include/effects',
        '../include/animator',
        '../include/views',
        '../include/xml',
        '../include/utils',
        '../include/images',
        '../src/utils',
      ],
      'sources': [
        '../include/animator/SkAnimator.h',
        '../include/animator/SkAnimatorView.h',

        '../src/animator/SkAnimate.h',
        '../src/animator/SkAnimateActive.cpp',
        '../src/animator/SkAnimateActive.h',
        '../src/animator/SkAnimateBase.cpp',
        '../src/animator/SkAnimateBase.h',
        '../src/animator/SkAnimateField.cpp',
        '../src/animator/SkAnimateMaker.cpp',
        '../src/animator/SkAnimateMaker.h',
        '../src/animator/SkAnimateProperties.h',
        '../src/animator/SkAnimateSet.cpp',
        '../src/animator/SkAnimateSet.h',
        '../src/animator/SkAnimator.cpp',
        '../src/animator/SkAnimatorScript.cpp',
        '../src/animator/SkAnimatorScript.h',
        #'../src/animator/SkAnimatorScript2.cpp', fails on windows
        #'../src/animator/SkAnimatorScript2.h',
        '../src/animator/SkBoundable.cpp',
        '../src/animator/SkBoundable.h',
        '../src/animator/SkBuildCondensedInfo.cpp',
        #'../src/animator/SkCondensedDebug.cpp', fails on windows
        #'../src/animator/SkCondensedRelease.cpp',
        '../src/animator/SkDisplayable.cpp',
        '../src/animator/SkDisplayable.h',
        '../src/animator/SkDisplayAdd.cpp',
        '../src/animator/SkDisplayAdd.h',
        '../src/animator/SkDisplayApply.cpp',
        '../src/animator/SkDisplayApply.h',
        '../src/animator/SkDisplayBounds.cpp',
        '../src/animator/SkDisplayBounds.h',
        '../src/animator/SkDisplayEvent.cpp',
        '../src/animator/SkDisplayEvent.h',
        '../src/animator/SkDisplayEvents.cpp',
        '../src/animator/SkDisplayEvents.h',
        '../src/animator/SkDisplayInclude.cpp',
        '../src/animator/SkDisplayInclude.h',
        '../src/animator/SkDisplayInput.cpp',
        '../src/animator/SkDisplayInput.h',
        '../src/animator/SkDisplayList.cpp',
        '../src/animator/SkDisplayList.h',
        '../src/animator/SkDisplayMath.cpp',
        '../src/animator/SkDisplayMath.h',
        '../src/animator/SkDisplayMovie.cpp',
        '../src/animator/SkDisplayMovie.h',
        '../src/animator/SkDisplayNumber.cpp',
        '../src/animator/SkDisplayNumber.h',
        '../src/animator/SkDisplayPost.cpp',
        '../src/animator/SkDisplayPost.h',
        '../src/animator/SkDisplayRandom.cpp',
        '../src/animator/SkDisplayRandom.h',
        '../src/animator/SkDisplayScreenplay.cpp',
        '../src/animator/SkDisplayScreenplay.h',
        '../src/animator/SkDisplayType.cpp',
        '../src/animator/SkDisplayType.h',
        '../src/animator/SkDisplayTypes.cpp',
        '../src/animator/SkDisplayTypes.h',
        '../src/animator/SkDisplayXMLParser.cpp',
        '../src/animator/SkDisplayXMLParser.h',
        '../src/animator/SkDraw3D.cpp',
        '../src/animator/SkDraw3D.h',
        '../src/animator/SkDrawable.cpp',
        '../src/animator/SkDrawable.h',
        '../src/animator/SkDrawBitmap.cpp',
        '../src/animator/SkDrawBitmap.h',
        '../src/animator/SkDrawBlur.cpp',
        '../src/animator/SkDrawBlur.h',
        '../src/animator/SkDrawClip.cpp',
        '../src/animator/SkDrawClip.h',
        '../src/animator/SkDrawColor.cpp',
        '../src/animator/SkDrawColor.h',
        '../src/animator/SkDrawDash.cpp',
        '../src/animator/SkDrawDash.h',
        '../src/animator/SkDrawDiscrete.cpp',
        '../src/animator/SkDrawDiscrete.h',
        '../src/animator/SkDrawEmboss.cpp',
        '../src/animator/SkDrawEmboss.h',
        '../src/animator/SkDrawExtraPathEffect.cpp',
        '../src/animator/SkDrawFull.cpp',
        '../src/animator/SkDrawFull.h',
        '../src/animator/SkDrawGradient.cpp',
        '../src/animator/SkDrawGradient.h',
        '../src/animator/SkDrawGroup.cpp',
        '../src/animator/SkDrawGroup.h',
        '../src/animator/SkDrawLine.cpp',
        '../src/animator/SkDrawLine.h',
        '../src/animator/SkDrawMatrix.cpp',
        '../src/animator/SkDrawMatrix.h',
        '../src/animator/SkDrawOval.cpp',
        '../src/animator/SkDrawOval.h',
        '../src/animator/SkDrawPaint.cpp',
        '../src/animator/SkDrawPaint.h',
        '../src/animator/SkDrawPath.cpp',
        '../src/animator/SkDrawPath.h',
        '../src/animator/SkDrawPoint.cpp',
        '../src/animator/SkDrawPoint.h',
        '../src/animator/SkDrawRectangle.cpp',
        '../src/animator/SkDrawRectangle.h',
        '../src/animator/SkDrawSaveLayer.cpp',
        '../src/animator/SkDrawSaveLayer.h',
        '../src/animator/SkDrawShader.cpp',
        '../src/animator/SkDrawShader.h',
        '../src/animator/SkDrawText.cpp',
        '../src/animator/SkDrawText.h',
        '../src/animator/SkDrawTextBox.cpp',
        '../src/animator/SkDrawTextBox.h',
        '../src/animator/SkDrawTo.cpp',
        '../src/animator/SkDrawTo.h',
        '../src/animator/SkDrawTransparentShader.cpp',
        '../src/animator/SkDrawTransparentShader.h',
        '../src/animator/SkDump.cpp',
        '../src/animator/SkDump.h',
        '../src/animator/SkExtras.h',
        '../src/animator/SkGetCondensedInfo.cpp',
        '../src/animator/SkHitClear.cpp',
        '../src/animator/SkHitClear.h',
        '../src/animator/SkHitTest.cpp',
        '../src/animator/SkHitTest.h',
        '../src/animator/SkIntArray.h',
        '../src/animator/SkMatrixParts.cpp',
        '../src/animator/SkMatrixParts.h',
        '../src/animator/SkMemberInfo.cpp',
        '../src/animator/SkMemberInfo.h',
        '../src/animator/SkOpArray.cpp',
        '../src/animator/SkOpArray.h',
        '../src/animator/SkOperand.h',
        '../src/animator/SkOperand2.h',
        '../src/animator/SkOperandInterpolator.h',
        '../src/animator/SkOperandIterpolator.cpp',
        '../src/animator/SkPaintParts.cpp',
        '../src/animator/SkPaintParts.h',
        '../src/animator/SkParseSVGPath.cpp',
        '../src/animator/SkPathParts.cpp',
        '../src/animator/SkPathParts.h',
        '../src/animator/SkPostParts.cpp',
        '../src/animator/SkPostParts.h',
        '../src/animator/SkScript.cpp',
        '../src/animator/SkScript.h',
        '../src/animator/SkScript2.h',
        '../src/animator/SkScriptCallBack.h',
        '../src/animator/SkScriptDecompile.cpp',
        '../src/animator/SkScriptRuntime.cpp',
        '../src/animator/SkScriptRuntime.h',
        '../src/animator/SkScriptTokenizer.cpp',
        '../src/animator/SkSnapshot.cpp',
        '../src/animator/SkSnapshot.h',
        '../src/animator/SkTDArray_Experimental.h',
        '../src/animator/SkTextOnPath.cpp',
        '../src/animator/SkTextOnPath.h',
        '../src/animator/SkTextToPath.cpp',
        '../src/animator/SkTextToPath.h',
        '../src/animator/SkTime.cpp',
        '../src/animator/SkTypedArray.cpp',
        '../src/animator/SkTypedArray.h',
        '../src/animator/SkXMLAnimatorWriter.cpp',
        '../src/animator/SkXMLAnimatorWriter.h',
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          '../include/animator',
        ],
      },
    },
  ],
}

# Local Variables:
# tab-width:2
# indent-tabs-mode:nil
# End:
# vim: set expandtab tabstop=2 shiftwidth=2:
