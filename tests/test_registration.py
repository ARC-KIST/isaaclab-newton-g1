# Copyright (c) 2022-2026, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

"""Tests for the generated task registrations."""

import gymnasium as gym

import g1_locomotion.tasks  # noqa: F401

CONFIG_MODULE = "g1_locomotion.tasks.locomotion.config.g1"


def test_task_registrations():
    """The generated tasks must expose valid environment and agent entry points."""
    expected = {
        "Unitree-G1-Velocity-Newton-Flat": {
            "entry_point": "isaaclab.envs:ManagerBasedRLEnv",
            "env_cfg_entry_point": f"{CONFIG_MODULE}.flat_env_cfg:G1FlatEnvCfg",
            "rsl_rl_cfg_entry_point": f"{CONFIG_MODULE}.agents.rsl_rl_ppo_cfg:G1FlatPPORunnerCfg",
            "default_agent": "rsl_rl",
        },
        "Unitree-G1-Velocity-Newton-Rough": {
            "entry_point": "isaaclab.envs:ManagerBasedRLEnv",
            "env_cfg_entry_point": f"{CONFIG_MODULE}.rough_env_cfg:G1RoughEnvCfg",
            "rsl_rl_cfg_entry_point": f"{CONFIG_MODULE}.agents.rsl_rl_ppo_cfg:G1RoughPPORunnerCfg",
            "default_agent": "rsl_rl",
        },
    }

    for task_id, expected_values in expected.items():
        spec = gym.spec(task_id)
        assert spec.entry_point == expected_values["entry_point"]
        assert spec.kwargs["env_cfg_entry_point"] == expected_values["env_cfg_entry_point"]
        assert spec.kwargs["rsl_rl_cfg_entry_point"] == expected_values["rsl_rl_cfg_entry_point"]
        assert spec.kwargs["default_agent"] == expected_values["default_agent"]
