import unittest
from engine.user_class.base.player_base import PlayerBase
from engine.core.internal.camera import Camera
from pygame.math import Vector2
from engine.core import config
from engine.game_display import MockDisplay
from engine.core.game_manager import MockManager
from engine.core.collision_handler import CollisionHandler

'''
Testing the creation and movimentation of the Player and the game camera
reaction to it's movement.

These tests are also important to show how the code is garbage and you need 
a shit ton of instatiations just to move the goddamn camera, so it's important
to leave the current system here, so I see this and think 'oh, I have to fix
this' and hopefully someday I will.
'''
class MyTest(unittest.TestCase):
    def setUp(self):
        self.game_manager = MockManager(MockDisplay((800, 600), 0))
        self.game_manager.hierarchy.append(PlayerBase())
        self.game_manager.main_camera = Camera(self.game_manager, Vector2(self.game_manager.game_display.get_size()) // 2, Vector2(1, 1))
        self.game_manager.collision_handler = CollisionHandler()

        self.player = self.game_manager.hierarchy[0]

        self.player._awake(self.game_manager.game_display, self.game_manager.main_camera)
        self.player._start()
        self.player.load_spritesheet('characters', 'frisk')

        #TODO: for some reason, the collision list is not empty when setUp is run once.
        # is needed to find a way to fix this.
        self.game_manager.collision_handler.collisions_list = []
        self.game_manager.collision_handler._append_if_has_collider(self.player)

    def testPlayerInstantiation(self):
        self.assertEqual(self.player.transform.position, Vector2(0, 0))

    def testPlayerPosition(self):
        self.player.transform.set_position(Vector2(10, 20))

        self.assertEqual(self.player.transform.position.x, 10)
        self.assertEqual(self.player.transform.position.y, 20)

    def testPlayerCameraPosition(self):
        self.assertEqual(self.game_manager.main_camera.transform.position == Vector2(400, 300), 
                        True)

    def testPlayerCameraVirtualPositionOrigin(self):
        self.player.main_camera.transform.set_position(Vector2(0, 0))
        self.player.transform.set_position(Vector2(0, 0))

        virtual_position = self.player._position_based_on_display_scale()
        self.assertEqual(virtual_position == Vector2(400, 300), True)

    def testPlayerCameraVirtualPositionMovePlayerNegative(self):
        self.player.transform.set_position(Vector2(-400, -300))
        self.game_manager.main_camera.transform.set_position(Vector2(0, 0))

        virtual_position = self.player._position_based_on_display_scale()

        self.assertEqual(virtual_position == Vector2(0, 0), True)

    def testPlayerCameraVirtualPositionMovePlayerPositive(self):
        self.player.transform.set_position(Vector2(400, 300))
        self.game_manager.main_camera.transform.set_position(Vector2(0, 0))

        virtual_position = self.player._position_based_on_display_scale()

        self.assertEqual(virtual_position == Vector2(800, 600), True)

    def testPlayerCameraVirtualPositionMoveCameraNegative(self):
        self.player.transform.set_position(Vector2(0, 0))
        self.game_manager.main_camera.transform.set_position(Vector2(-400, -300))

        virtual_position = self.player._position_based_on_display_scale()

        self.assertEqual(virtual_position == Vector2(800, 600), True)

    def testPlayerCameraVirtualPositionMoveCameraPositive(self):
        self.player.transform.set_position(Vector2(0, 0))
        self.game_manager.main_camera.transform.set_position(Vector2(400, 300))

        virtual_position = self.player._position_based_on_display_scale()

        self.assertEqual(virtual_position == Vector2(0, 0), True)

    def testPlayerCameraVirtualPositionMovePlayerAndCamera(self):
        self.player.transform.set_position(Vector2(-400, -300))
        self.game_manager.main_camera.transform.set_position(Vector2(400, 300))

        virtual_position = self.player._position_based_on_display_scale()

        self.assertEqual(virtual_position == Vector2(-400, -300), True)

    def testPlayerCameraVirtualPositionCameraFollowPlayer(self):
        self.player.transform.set_position(Vector2(800, 600))
        self.game_manager.main_camera.transform.set_position(Vector2(800, 600))

        virtual_position = self.player._position_based_on_display_scale()

        self.assertEqual(virtual_position == Vector2(400, 300), True)
