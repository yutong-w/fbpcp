# Copyright (c) Meta Platforms, Inc. and affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

# pyre-strict

from enum import Enum


class MPCRoles(Enum):
    PUBLISHER = "PUBLISHER"
    PARTNER = "PARTNER"
