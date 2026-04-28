def checkmate(board : str):
    grid = board.split('\n')
    size = len(grid)

    if size == 0 :
        return 
    
    for row in grid :
        if len(row) != size :
            print ('Error ,this board is not square')
            return
        
    king_pos = None 
    for i in range (size) :
        for j in range (size) :
           if grid[i][j] == "K" :
               king_pos = (i,j)
               break

    if king_pos is None :
        return

    def in_bounds (x,y) :
        return 0 <= x < size and 0 <= y < size
    
    kx ,ky = king_pos

    for dx,dy in [(-1,-1),(-1,1)] : #pawn
        x,y = kx+dx , ky+dy 
        if in_bounds(x,y) and grid[x][y] == "P" :
            print ('Success')
            return
    for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)] : #Rook or queen
        x,y = kx,ky
        while True :
            x += dx
            y += dy
            if not in_bounds(x,y) :
                break
            piece = grid[x][y]
            if piece != "." :
                if piece in ("R","Q") :
                    print ('Success')
                    return
                break
    for dx , dy in [(1,1),(1,-1),(-1,1),(-1,-1)]: #bishop or queen
        x,y = kx,ky 
        while True :
            x += dx
            y += dy
            if not in_bounds(x,y) :
                break
            piece = grid[x][y]
            if piece != "." :
                if piece in ("B" , "Q") :
                    print ('Success')
                    return
                break
    print ("Faill")