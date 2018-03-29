if [[ $EUID -ne 0 ]]; then
    echo "This script must be run as root" 1>&2
    exit 1
fi

# remove old settings
rm /etc/nginx/sites-enabled/test.conf
rm /etc/nginx/sites-enabled/default

# clean project dir
rm /home/box/web/uploads/.empty 2> /dev/null
rm /home/box/web/public/css/.empty 2> /dev/null
rm /home/box/web/public/img/.empty 2> /dev/null
rm /home/box/web/public/js/.empty  2> /dev/null
rm -rf /home/box/etc 2> /dev/null

# set access rigts on folders
chown -R www-data /home/box/web/uploads
chown -R www-data /home/box/web/public
chmod -R 755 /home/box/web/uploads
chmod -R 755 /home/box/web/public

# copy nginx configuration
ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf

# copy gunicorn configuration
mkdir /home/box/etc
chmod -R 755 /home/box/etc
cp /home/box/web/etc/hello.py /home/box/etc
ln -s /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py

# restart servers
/etc/init.d/gunicorn restart
/etc/init.d/nginx restart
