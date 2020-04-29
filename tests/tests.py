import os
import unittest
import subprocess
import nbformat

                
class NotebookTestsMeta(type):
    
    @staticmethod
    def get_notebooks():
        result = []
        for r, d, f in os.walk('.'):
            if '.git' in d:
                continue
            for file in f:
                if '.ipynb' in file and not '-checkpoint' in file:
                    test_name = str.replace(str.replace(str.replace(str(os.path.join(r, file)),'.ipynb',''),'.',''),'\\','_')
                    result.append( (os.path.join(r, file), test_name,))
        return result
    
    def __new__(cls, name, bases, attrs):
        notebooks = NotebookTestsMeta.get_notebooks()
        for x in notebooks:
            attrs['test_%s' % x[1]] = cls.gen(x[0])
        return super(NotebookTestsMeta, cls).__new__(cls, name, bases, attrs)
    
    @staticmethod
    def _notebook_run(path):
        """Execute a notebook via nbconvert and collect output.
           :returns (parsed nb object, execution errors)
        """
        dirname, nb_name = os.path.split(path)
        curr_dir = os.getcwd()
        os.chdir(dirname)
        args = ["jupyter", "nbconvert", "--to", "notebook", "--execute",
                "--ExecutePreprocessor.timeout=600",
                "--output", 'tmp.ipynb', nb_name]  # fout.name, path]
        FNULL = open(os.devnull, 'w')
        try:
            subprocess.check_call(args, stdout=FNULL, stderr=subprocess.STDOUT)
        except:
            os.chdir(curr_dir)
            return ['An error occured converting notebook with nbconvert'] 
        f = open('tmp.ipynb', 'r')
        nb = nbformat.read(f, nbformat.current_nbformat)
        errors = [output for cell in nb.cells if "outputs" in cell
                  for output in cell["outputs"]
                  if output.output_type == "error"]
        f.close()
        os.remove('tmp.ipynb')
        os.chdir(curr_dir)
        return errors

    @classmethod
    def gen(cls, notebook_file):
        # Return a testcase that tests ``x``.
        def fn(self):
            errors = NotebookTestsMeta._notebook_run(notebook_file)
            self.assertTrue(errors == [])
        return fn

    
    
class NotebookTests(unittest.TestCase, metaclass = NotebookTestsMeta):
    
    def test_depp(self):
        self.assertEqual(0,0)

if __name__ == '__main__':
    unittest.main()
