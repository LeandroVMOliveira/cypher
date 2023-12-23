import requirements
def cyphers(n):
    match n:
        case 1: 
            requirements.caesar.main()
            return
        case 2:
            requirements.az26.main()
            return
        case 3:
            requirements.base64.main()
            return
        case 4:
            requirements.binary.main()
            return
        case 5:
            requirements.hex.main()
            return 
        case default:
            print(0)
            return 0