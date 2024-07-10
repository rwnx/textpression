#!/usr/bin/env python3
import typer
from rich import print

app = typer.Typer()


source_map = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!?"
small_map = "ᵃᵇᶜᵈᵉᶠᵍʰᶦʲᵏˡᵐⁿᵒᵖᵠʳˢᵗᵘᵛʷˣʸᶻᴬᴮᶜᴰᴱᶠᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾᵠᴿˢᵀᵁⱽᵂˣʸᶻ¹²³⁴⁵⁶⁷⁸⁹⁰ᵎˀ"
sub_map = "ₐᵦ𝒸𝒹ₑ𝒻𝓰ₕᵢⱼₖₗₘₙₒₚᵩᵣₛₜᵤᵥ𝓌ₓᵧ𝓏ₐBCDₑFGₕᵢⱼₖₗₘₙₒₚQᵣₛₜᵤᵥWₓYZ₁₂₃₄₅₆₇₈₉₀!?"
smallcaps_map = "ᴀʙᴄᴅᴇғɢʜɪᴊᴋʟᴍɴᴏᴘǫʀsᴛᴜᴠᴡxʏᴢABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!?"

def source_subst(source: str, target: str, input: str) -> str: 
    output = []
    for char in input:
        try:
          output.append(target[source.index(char)])
        except ValueError:
            output.append(char)
    return "".join(output)

@app.command()
def small(all: list[str]):
  input = " ".join(all)
  print(source_subst(source_map, small_map, input))

@app.command()
def sub(all: list[str]):
  input = " ".join(all)
  print(source_subst(source_map, sub_map, input))


@app.command()
def smallcaps(all: list[str]):
  input = " ".join(all)
  print(source_subst(source_map, smallcaps_map, input))

@app.command()
def all(all: list[str]):
  input = " ".join(all)
  print(source_subst(source_map, small_map, input))
  print(source_subst(source_map, sub_map, input))
  print(source_subst(source_map, smallcaps_map, input))


if __name__ == "__main__":
    app()