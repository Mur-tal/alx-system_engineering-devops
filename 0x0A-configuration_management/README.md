# 0x0A. Configuration management
#### DevOps, SysAdmin, Scripting, CI/CD
This is a configuration management using Puppet
##### Install puppet
```
$ apt-get install -y ruby=1:2.7+1 --allow-downgrades
$ apt-get install -y ruby-augeas
$ apt-get install -y ruby-shadow
$ apt-get install -y puppet
```
Puppet-lint is a style-guide for puppet manifest
##### Check that your Puppet manifest conform to the style guide
1st install the puppet-lint using manifest or CLI thus

```
package { 'puppet-lint':
  ensure   => '1.1.0',
  provider => 'gem',
}
```

or

```
$ gem install puppet-lint
```

##### Run It!
```
$ puppet-lint /etc/puppet/modules
foo/manifests/bar.pp - ERROR: trailing whitespace found on line 1
apache/manifests/server.pp - WARNING: variable not enclosed in {} on line 56
```
##### Fix Them!
```
$ puppet-lint --fix /etc/puppet/modules
foo/manifests/bar.pp - FIXED: trailing whitespace found on line 1
apache/manifests/server.pp - FIXED: variable not enclosed in {} on line 56
```
Helpful [link](http://puppet-lint.com/)
Head on over to the checks [page](http://puppet-lint.com/checks/) to see a description of each check and get some help on how to clear those errors.
