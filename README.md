# log__analysis
This is the third project log_analysis, Udacity Full Stack Nanodegree course using the quaries of postgres database.
##For do this project we should install certain softwares as: --virtualBox
 --vagrant
 --python3
 --postgres database
 ##vagrant is used run different operating system environment on single os.
 ##This project is completely based on ubuntu os.
 ##After installing vagrant we should create a folder name vagrant in our directory.Later we open the command propmt or terminal in the vagrant folder path.
 ##Then should run these commands:--vagrant -v -> to know the version
 --vagrant init ubuntu/trusty64 -> to vagrant environment for ubuntu.
 --vagrant up ->to launch virtual mechine.
 --vagrant ssh ->log into this ssh.
 --sudo apt-get install python-psycopg2.
 --sudo -i -u postgres ->to change the postgres database.
 --psql ->to  connect the postgres database.
 --\l ->to display the files in directory.
 ##Create user name with password then enter \du to see the roles command.
 ##Here we can see different roles like Superuser,Createrole,CreateDB.For creating these roles we use quires...
 --alter user name with Superuser;
 --alter user username with Createrole;
 --alter user username with CreateDB; 
 --\q to exit .
 --sudo -i -u vagrant to database changes to vagrant.
 --psql and then create database news.
 --run \c news to change database to news.
 ##For do this project we have a data we should download the newsdata zipfile  and fetch the data to the sql.
 ##Run command   psql -d news -f newsdata.sql
 ##In this news data we have 3 tables named as articles, authors, log.
 ##In this first asked most popular three articles in all the time.for that i created view as 
 create view article_views as select title, author, count(title) as views from articles, log where log.path like concat('%',articles.slug) group by articles.title, articles.author order by views desc;
 ##Then asked most popular article all the time for that i wrote query as
 create view author_view as select name,count(articles.author) as views from articles, authors, log where log.path like concat('%',articles.slug) and articles.author=authors.id group by authors.name order by views desc;
  ##For calculate more than 1% 
  create view log_view as select date(time), round(100.0*sum(case log.status when '200 OK' then 0 else 1 end)/count(log.status),2) as Error_Percent from log group by date(time) order by Error_Percent desc;
  ##all of these commands run on vagrant.
  #after create a python file should run on vagrant.
