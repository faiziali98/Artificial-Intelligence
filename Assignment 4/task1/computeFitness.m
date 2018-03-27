function [ fitness ] = computeFitness( image1, originalImage )
    [rows, columns, rgb] = size(image1);
    fitness = 0;
    for rgb=1:3
        for row=1:rows
            for column=1:columns
                fitness = fitness + abs(double(image1(row,column,rgb)) - double(originalImage(row,column,rgb)));
            end
        end
    end
end

