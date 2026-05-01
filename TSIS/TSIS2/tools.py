from collections import deque


def flood_fill(surface, x, y, new_color):
    width, height = surface.get_size()

    try:
        old_color = surface.get_at((x, y))
    except:
        return

    if old_color == new_color:
        return

    queue = deque()
    queue.append((x, y))

    while queue:
        cx, cy = queue.popleft()

        if 0 <= cx < width and 0 <= cy < height:
            if surface.get_at((cx, cy)) == old_color:
                surface.set_at((cx, cy), new_color)

                queue.append((cx+1, cy))
                queue.append((cx-1, cy))
                queue.append((cx, cy+1))
                queue.append((cx, cy-1))