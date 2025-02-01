import time
import ascii_art as ASCII


def get_line_count_and_max_length(lines: list[str]) -> tuple[int, int]:
    """Avoir le nombre de ligne d'un texte et le nombre maximum de caractères

    Args:
        lines (list[str]): Texte sur plusieurs ligne sous forme de liste

    Returns:
        tuple[int, int]: nombre de ligne, nombre maximum de caractères
    """
    line_count = len(lines)
    max_length = max(len(line) for line in lines) if lines else 0
    return line_count, max_length


def print_inline(item : str) -> None:
    """Affichage (print) sans nouvelle ligne

    Args:
        item (str): élément à afficher
    """
    print(item, end="")

def display_vertical_text(text : str, pause=0.1) -> None:
    """Affiche un texte progressivement à la verticale.

    Args:
        text (str): Texte sur plusieurs lignes
        pause (float, optional): délai d'attente pour l'affichage. Defaults to 0.2.
    """
    
    lines = text.split("\n") # séparer chaque ligne du texte
    
    print_inline("\033[?25l") # désactiver le curseur
    print_inline("\033[6;92m") # clignotement et texte en vert
    
    nb_ligne, max_char  = get_line_count_and_max_length(lines)
    
    for col in range(max_char):
        for line in lines:
            print(line[:col]) # Affichage partiel de chaque ligne
        
        time.sleep(pause)
        print_inline(f"\033[{nb_ligne}A") # remonter au début de l'affichage
    
    print_inline(f"\033[0m{text}") # affichage final
    print_inline("\033[?25h") # réactive le curseur


if __name__ == "__main__":
    # TEST
    display_vertical_text(ASCII.MAP)

# @DevByDelta
