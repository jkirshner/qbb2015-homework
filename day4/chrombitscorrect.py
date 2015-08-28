import numpy
import copy

class ChromosomeLocationBitArrays( object ):

    def __init__( self, dicts=None, fname=None ):
        # If dicts parameter provided, use to initialize
        if dicts is not None:
            arrays = dicts
        else:
            arrays = {}
        # If fname parameter provided, initialize from file
        if fname is not None: 
            for line in open( fname ):
                fields = line.split()
                name = fields[0]
                size = int( fields[1] )
                arrays[name] = numpy.zeros( size, dtype=bool )
        self.arrays = arrays

    def set_bits_from_file( self, fname ):
        for line in open( fname ):
            fields = line.split()
            # Parse fields
            chrom = fields[0]
            start = int( fields[1] )
            end = int( fields[2] )
            self.arrays[ chrom ][ start : end ] = 1
        
    def intersect( self, other ):
        rval = {}
        for chrom in self.arrays:
            rval[chrom] = self.arrays[chrom] & other.arrays[chrom]
        return ChromosomeLocationBitArrays( dicts=rval )
        
    def union( self, other ):
        rval = {}
        for chrom in self.arrays:
            rval[chrom] = self.arrays[chrom] | other.arrays[chrom]
        return ChromosomeLocationBitArrays( dicts=rval )
        
    def complement( self ):
        rval = {}
        for chrom in self.arrays:
            rval[chrom] = ~ self.arrays[chrom]
        return ChromosomeLocationBitArrays( dicts=rval )
        
    def copy( self ):
        return ChromosomeLocationBitArrays( 
            dicts=copy.deepcopy( self.arrays ) )
            
    def bedmaker(self):
        rval = []
        counter = 0
        for chrom in self.arrays:
            startPosition = 0
            readingBool = False
            for index in self.arrays[chrom]:
                counter +=1
                if counter%250000==0:
                    print counter
                if index == 1:
                    counter +=1
                    
                    startPostion = counter
                    readingBool = True
                if readingBool == True:
                    if index == 0:
                        rval.append((chrom,startPosition,counter-1))
                        readingBool = False
                counter += 1  
        return rval
                
                