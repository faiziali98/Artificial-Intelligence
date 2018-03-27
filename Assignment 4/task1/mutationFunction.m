function [ rimage ] = mutationFunction( rimage )

    [rows,columns,rgb] = size(rimage{1});
    for i=1:6
        currentImage = rimage{i};
        for rgb=1:3
            for row=1:rows
                for column=1:columns
                    if(rand(i)>=0.99)
                        currentImage(row,column,rgb) = randi([0,255],1);
                    end
                end
            end
        end
        rimage{i} = currentImage;
    end
end

