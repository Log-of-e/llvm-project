//===-- HelloWorld.cpp - Example Transformations --------------------------===//
//
// Part of the LLVM Project, under the Apache License v2.0 with LLVM Exceptions.
// See https://llvm.org/LICENSE.txt for license information.
// SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
//
//===----------------------------------------------------------------------===//

#include "llvm/Transforms/HelloNew/HelloWorld.h"

using namespace llvm;

PreservedAnalyses HelloWorldPass::run(Function &F,
                                      FunctionAnalysisManager &AM) {
  
  
  outs() << "{ " ;

  outs() << "\"function\": \"" << F.getName() << "\", ";

  outs() << "\"rettype\": " << F.getReturnType()->getTypeID() << ", ";
  
  outs() << "\"cconv\": " << F.getCallingConv() << ", ";

  outs() << "\"isns\": " << F.getInstructionCount() ;

  outs() << " }," ;
  
  return PreservedAnalyses::all();
}
