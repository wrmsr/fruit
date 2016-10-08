#!/usr/bin/env python3
#  Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from fruit_test_common import *

def test_error_not_base():
    expect_compile_error(
    'NotABaseClassOfError<X,int>',
    'I is not a base class of C.',
    '''
struct X {};

Component<int> getComponent() {
  return fruit::createComponent()
    .bind<X, int>();
}
''')

def test_error_not_base_with_annotations():
    expect_compile_error(
    'NotABaseClassOfError<X,int>',
    'I is not a base class of C.',
    '''
struct Annotation {};
struct X {};

Component<fruit::Annotated<Annotation, int>> getComponent() {
  return fruit::createComponent()
    .bind<fruit::Annotated<Annotation, X>, fruit::Annotated<Annotation, int>>();
}
''')

def test_error_bound_to_itself():
    expect_compile_error(
    'InterfaceBindingToSelfError<X>',
    'The type C was bound to itself.',
    '''
struct X {};

Component<int> getComponent() {
  return fruit::createComponent()
    .bind<X, X>();
}
''')

if __name__ == '__main__':
    import nose2
    nose2.main()
