class GameStats:
    """Track statistics for Jordiz Invasion"""

    def __init__(self, ji_game):
        """Initialize statistics."""
        self.settings = ji_game.settings
        self.reset_stats()
        # Start Jordiz Invasion in an active state
        self.game_active = False

        # High score should never be reset
        self.high_score = 0

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
