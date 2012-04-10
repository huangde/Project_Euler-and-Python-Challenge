if __name__ == '__main__':
    step=2
    matrix_size=1
    end_term=1
    SpiralSum=end_term
    while matrix_size!=1001:
        SpiralSum+=(end_term+step)*4+6*step
        end_term+=4*step
        matrix_size+=2
        step+=2
        print end_term,matrix_size,SpiralSum
    print SpiralSum

