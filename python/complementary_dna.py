def DNA_strand(dna):
    complement = ""

    for nucleotide in dna:
        match nucleotide:
            case "A":
                complement += "T"
            case "T":
                complement += "A"
            case "G":
                complement += "C"
            case "C":
                complement += "G"

    return complement
