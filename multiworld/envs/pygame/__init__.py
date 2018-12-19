from gym.envs.registration import register
import logging

LOGGER = logging.getLogger(__name__)

_REGISTERED = False


def register_custom_envs():
    global _REGISTERED
    if _REGISTERED:
        return
    _REGISTERED = True

    LOGGER.info("Registering multiworld pygame gym environments")
    register(
        id='Point2DLargeEnv-offscreen-v0',
        entry_point='multiworld.envs.pygame.point2d:Point2DEnv',
        tags={
            'git-commit-hash': '166f0f3',
            'author': 'Vitchyr'
        },
        kwargs={
            'images_are_rgb': True,
            'target_radius': 1,
            'ball_radius': 1,
            'render_onscreen': False,
        },
    )
    register(
        id='Point2DLargeEnv-onscreen-v0',
        entry_point='multiworld.envs.pygame.point2d:Point2DEnv',
        tags={
            'git-commit-hash': '166f0f3',
            'author': 'Vitchyr'
        },
        kwargs={
            'images_are_rgb': True,
            'target_radius': 1,
            'ball_radius': 1,
            'render_onscreen': True,
        },
    )

    register(
        id='Point2DWallEnv-easy-u-v0',
        entry_point='multiworld.envs.pygame.point2d:Point2DWallEnv',
        tags={
            'git-commit-hash': '7a95dff', #'9cab5da',
            'author': 'Soroush'
        },
        kwargs={
            'action_scale': 0.25,
            'wall_shape': 'easy-u',
            'wall_thickness': 0.50,
            'render_size': 200,
            'images_are_rgb': True,
            'sample_realistic_goals': True,
            'norm_order': 2,
            'reward_type': 'vectorized_dense',
        },
    )

    register(
        id='Point2DWallEnvBox-v0',
        entry_point='multiworld.envs.pygame.point2d:Point2DWallEnv',
        tags={
            'git-commit-hash': '7a95dff', #'9cab5da',
            'author': 'Soroush'
        },
        kwargs={
            'action_scale': 0.25,
            'wall_shape': 'box',
            'wall_thickness': 2.0,
            'render_size': 48,
            'images_are_rgb': True,
            'sample_realistic_goals': True,
            'render_target': False,
            'norm_order': 2,
            'reward_type': 'dense',
            'ball_low': (-4, 3.90),
            'ball_high': (-3.90, 4),
        },
    )

    register(
        id='Image84Point2DWallEnvEasyU-v0',
        entry_point=create_image_84_point2d_wall_easy_u_v0,
        tags={
            'git-commit-hash': '7a95dff', #'9cab5da',
            'author': 'Soroush'
        },
    )

    register(
        id='Image84Point2DWallEnvEasyU-v1',
        entry_point=create_image_84_point2d_wall_easy_u_v1,
        tags={
            'git-commit-hash': '7a95dff', #'9cab5da',
            'author': 'Soroush'
        },
    )

    register(
        id='Image84Point2DWallEnv-v0',
        entry_point=create_image_84_point2d_wall_v0,
        tags={
            'git-commit-hash': '7a95dff', #'9cab5da',
            'author': 'Soroush'
        },
    )

    register(
        id='Point2DWallEnvFlappyBird-v0',
        entry_point='multiworld.envs.pygame.point2d:Point2DWallEnv',
        tags={
            'git-commit-hash': '7a7fafc', #'9cab5da',
            'author': 'Soroush'
        },
        kwargs={
            'action_scale': 0.25,
            'wall_shape': 'flappy-bird',
            'wall_thickness': 0.50,
            'render_size': 200,
            'images_are_rgb': True,
            'sample_realistic_goals': True,
            'norm_order': 2,
            'reward_type': 'vectorized_dense',
        },
    )

    register(
        id='Image84Point2DWallEnvFlappyBird-v0',
        entry_point=create_image_84_point2d_wall_flappy_bird_v0,
        tags={
            'git-commit-hash': '7a7fafc', #'9cab5da',
            'author': 'Soroush'
        },
    )

    register(
        id='Image84Point2DWallEnvFlappyBird-v1',
        entry_point=create_image_84_point2d_wall_flappy_bird_v1,
        tags={
            'git-commit-hash': '7a7fafc', #'9cab5da',
            'author': 'Soroush'
        },
    )

    register(
        id='Image84Point2DWallEnvFlappyBird-v2',
        entry_point=create_image_84_point2d_wall_flappy_bird_v2,
        tags={
            'git-commit-hash': '9676f61', #'9cab5da',
            'author': 'Soroush'
        },
    )

def create_image_84_point2d_wall_flappy_bird_v0():
    from multiworld.core.image_env import ImageEnv
    from multiworld.envs.pygame.point2d import Point2DWallEnv

    kwargs = {
        'action_scale': 0.25,
        'wall_shape': 'flappy-bird',
        'wall_thickness': 0.50,
        'render_target': False,
        'render_size': 84,
        'images_are_rgb': True,
        'sample_realistic_goals': True,
        'norm_order': 2,
        'reward_type': 'vectorized_dense',
    }
    wrapped_env = Point2DWallEnv(**kwargs)
    return ImageEnv(
        wrapped_env,
        84,
        init_camera=None,
        transpose=True,
        normalize=True,
        non_presampled_goal_img_is_garbage=False,
    )

def create_image_84_point2d_wall_flappy_bird_v1():
    from multiworld.core.image_env import ImageEnv
    from multiworld.envs.pygame.point2d import Point2DWallEnv

    kwargs = {
        'action_scale': 0.25,
        'wall_shape': 'flappy-bird',
        'wall_thickness': 0.50,
        'render_target': False,
        'render_size': 84,
        'images_are_rgb': True,
        'sample_realistic_goals': True,
        'norm_order': 2,
        'reward_type': 'vectorized_dense',
        'ball_low': (-3.5, -1.5),
        'ball_high': (-3, 0.5),
        'goal_low': (3, -0.5),
        'goal_high': (3.5, 1.5),
    }
    wrapped_env = Point2DWallEnv(**kwargs)
    return ImageEnv(
        wrapped_env,
        84,
        init_camera=None,
        transpose=True,
        normalize=True,
        non_presampled_goal_img_is_garbage=False,
    )

def create_image_84_point2d_wall_flappy_bird_v2():
    from multiworld.core.image_env import ImageEnv
    from multiworld.envs.pygame.point2d import Point2DWallEnv

    kwargs = {
        'action_scale': 0.25,
        'wall_shape': 'flappy-bird',
        'wall_thickness': 0.50,
        'render_target': False,
        'render_size': 84,
        'images_are_rgb': True,
        'sample_realistic_goals': True,
        'norm_order': 2,
        'reward_type': 'vectorized_dense',
        'ball_low': (-3.5, -3.0),
        'ball_high': (-3, -0.5),
        'goal_low': (3, 0.5),
        'goal_high': (3.5, 3.0),
    }
    wrapped_env = Point2DWallEnv(**kwargs)
    return ImageEnv(
        wrapped_env,
        84,
        init_camera=None,
        transpose=True,
        normalize=True,
        non_presampled_goal_img_is_garbage=False,
    )

def create_image_84_point2d_wall_easy_u_v0():
    from multiworld.core.image_env import ImageEnv
    from multiworld.envs.pygame.point2d import Point2DWallEnv

    kwargs = {
        'action_scale': 0.25,
        'wall_shape': 'easy-u',
        'wall_thickness': 0.50,
        'render_target': False,
        'render_size': 84,
        'images_are_rgb': True,
        'sample_realistic_goals': True,
        'norm_order': 2,
        'reward_type': 'vectorized_dense',
    }
    wrapped_env = Point2DWallEnv(**kwargs)
    return ImageEnv(
        wrapped_env,
        84,
        init_camera=None,
        transpose=True,
        normalize=True,
        non_presampled_goal_img_is_garbage=False,
    )

def create_image_84_point2d_wall_easy_u_v1():
    from multiworld.core.image_env import ImageEnv
    from multiworld.envs.pygame.point2d import Point2DWallEnv

    kwargs = {
        'action_scale': 0.25,
        'wall_shape': 'easy-u',
        'wall_thickness': 0.50,
        'render_target': False,
        'render_size': 84,
        'images_are_rgb': True,
        'sample_realistic_goals': True,
        'norm_order': 2,
        'reward_type': 'vectorized_dense',
        'ball_low': (-2, -0.5),
        'ball_high': (2, 1),
        'goal_low': (-4, 2),
        'goal_high': (4, 4),
    }
    wrapped_env = Point2DWallEnv(**kwargs)
    return ImageEnv(
        wrapped_env,
        84,
        init_camera=None,
        transpose=True,
        normalize=True,
        non_presampled_goal_img_is_garbage=False,
    )

def create_image_84_point2d_wall_v0():
    from multiworld.core.image_env import ImageEnv
    from multiworld.envs.pygame.point2d import Point2DWallEnv

    kwargs = {
        'action_scale': 0.25,
        'wall_shape': 'none',
        'render_target': False,
        'render_size': 84,
        'images_are_rgb': True,
        'norm_order': 2,
        'reward_type': 'vectorized_dense',
    }
    wrapped_env = Point2DWallEnv(**kwargs)
    return ImageEnv(
        wrapped_env,
        84,
        init_camera=None,
        transpose=True,
        normalize=True,
        non_presampled_goal_img_is_garbage=False,
    )


register_custom_envs()
