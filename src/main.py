import pygame as pg
import asyncio

async def main():
    count = 60

    while True:
        print("Test")
        pg.display.update()

        await asyncio.sleep(0)

        if count <= 0:
            pg.quit()
            return
        
        count -= 1
        clock.tick(60)

if __name__ == "__main__":
    pg.init()
    pg.display.set_mode((320, 240))
    clock = pg.time.Clock()

    main()