function [ image1 ] = crossOver( image1, image2 )
% Perform crossOver between the two provided images
    [rows, columns, rgb] = size(image1);
    if(rand > 0.1)
        crossOverRow = randi([1 rows],1);
        for rgb=1:3
            tempStore = image1(crossOverRow:rows,1:columns,rgb);
            image1(crossOverRow:rows,1:columns,rgb) = image2(crossOverRow:rows,1:columns,rgb);
            image2(crossOverRow:rows,1:columns,rgb) = tempStore;
        end
    end
end

