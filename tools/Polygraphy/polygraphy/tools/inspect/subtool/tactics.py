#
# SPDX-FileCopyrightText: Copyright (c) 1993-2024 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from polygraphy import mod
from polygraphy.logger import G_LOGGER
from polygraphy.tools.base import Tool

algorithm_selector = mod.lazy_import("polygraphy.backend.trt.algorithm_selector")


class Tactics(Tool):
    """
    Display the contents of Polygraphy tactic replay files, such as the ones
    generated by `--save-tactics`, in a human readable format.
    """

    def __init__(self):
        super().__init__("tactics")

    def add_parser_args(self, parser):
        parser.add_argument("tactic_replay", help="Path to a tactic replay file")

    def run_impl(self, args):
        replay = algorithm_selector.TacticReplayData.load(args.tactic_replay)
        G_LOGGER.info(replay)
