export cdir=$(pwd)
find | while read dir
do
    if [ -d $dir ] ; then
        cd ./$dir
        inary bi
        cd $cdir
    fi
done
