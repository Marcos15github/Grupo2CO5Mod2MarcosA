import pygame


class BulletManager:
    def __init__(self, enemy_manager):
        self.bullets = []
        self.enemy_bullets = []    
        self.explosion_image = pygame.image.load("explosion1.png")  # Carga la imagen de explosión
        self.enemy_manager = None

    def set_enemy_manager(self, enemy_manager):
        self.enemy_manager = enemy_manager
        
    def update (self, game):

        for bullet in self.bullets:
            bullet.update(self.bullets)

            for enemy in game.enemy_manager.enemies:
                if bullet.rect.colliderect(enemy.rect) and bullet.owner == 'player':
                    #explosion_sound.play()
                    self.explosion_index = 0
                    game.score += 100
                    game.enemy_manager.enemies.remove(enemy)
                    self.bullets.remove(bullet)
                    self.show_explosion(enemy.rect.center)  # Muestra la explosión en la posición del enemigo
                    
        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)

            if bullet.rect.colliderect(game.player.rect) and bullet.owner == 'enemy':
                game.death_count += 1
                
                self.enemy_bullets.remove(bullet)
                game.playing = False
                pygame.time.delay(1000)
                break

    def draw (self, screen):
        for bullet in self.bullets:
            bullet.draw(screen)

        for bullet in self.enemy_bullets:
            bullet.draw(screen)

    def add_bullet(self, bullet):
        if bullet.owner == 'player' and len(self.bullets) < 3:
            self.bullets.append(bullet)
        elif bullet.owner == 'enemy' and len(self.enemy_bullets) < 1:
            self.enemy_bullets.append(bullet)
    
    def reset(self):
        self.bullets = []
        self.enemy_bullets = []

    def show_explosion(self, position):
        self.screen.blit(self.explosion_image, position)  # Muestra la imagen de explosión en la posición indicada