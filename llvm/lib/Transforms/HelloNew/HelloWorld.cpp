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
  
  outs() << "Start HelloWorldPass" << "\n";

  outs() << " name: " << F.getName() << "\n";

  outs() << "  TypeID of Return Type:   " << F.getReturnType()->getTypeID() << "\n";
  
  outs() << "   Calling Convention:  " << F.getCallingConv() << "\n";

  outs() << "   Instruction Count:  " << F.getInstructionCount() << "\n";

  outs() << "End HelloWorldPass" << "\n";
  
  return PreservedAnalyses::all();
}
