def make_readable(seconds):
    sec = seconds % 60
    minutes = ((seconds - sec) // 60) % 60
    hours = (((seconds - sec) // 60) - minutes) // 60
    return f"{hours:02}:{minutes:02}:{sec:02}"
