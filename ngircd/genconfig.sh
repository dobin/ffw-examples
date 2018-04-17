#!/bin/bash

processCount=32
configTemplate="ffw-ngircd-sample.conf"
replaceString="FFWPORT"
startPort=6667

n=0
while [ $n -lt $processCount ]; do
    let port=$startPort+$n
    newFilename="bin/ffw-ngircd-$port.conf"

    cp $configTemplate $newFilename
    sed -i "s/$replaceString/$port/" $newFilename
    let n=n+1
done
